const express = require("express");
const cors = require("cors");
const { Pool } = require("pg");
require("dotenv").config();
console.log(process.env.DATABASE_URL);

const app = express();
app.use(cors());
app.use(express.json());

const pool = new Pool({
  connectionString: process.env.DATABASE_URL,
  ssl: false,
});

// Ensure 'likes' column exists with default value 0
pool.query("ALTER TABLE guestbook ADD COLUMN IF NOT EXISTS likes INTEGER DEFAULT 0");

// Add a new entry
app.post("/api/guestbook", async (req, res) => {
  const { name, message, password } = req.body;
  try {
    const result = await pool.query(
      "INSERT INTO guestbook (name, message, password, likes) VALUES($1, $2, $3, 0) RETURNING *",
      [name, message, password]
    );
    res.json(result.rows[0]);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Get all entries
app.get("/api/guestbook", async (req, res) => {
  const { sort } = req.query;
  try {
    let query = "SELECT id, name, message, created_at, likes FROM guestbook";
    if (sort === "likes") {
      query += " ORDER BY likes DESC, created_at DESC";
    } else {
      query += " ORDER BY created_at DESC";
    }
    const result = await pool.query(query);
    res.json(result.rows);
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Update an entry
app.put("/api/guestbook/:id", async (req, res) => {
  const { id } = req.params;
  const { message, password } = req.body;
  try {
    const result = await pool.query("SELECT password FROM guestbook WHERE id = $1", [id]);
    if (result.rows.length > 0 && result.rows[0].password === password) {
      const updateResult = await pool.query(
        "UPDATE guestbook SET message = $1 WHERE id = $2 RETURNING id, name, message, created_at, likes",
        [message, id]
      );
      res.json(updateResult.rows[0]);
    } else {
      res.status(403).json({ error: "비밀번호가 일치하지 않습니다." });
    }
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Delete an entry
app.delete("/api/guestbook/:id", async (req, res) => {
  const { id } = req.params;
  const { password } = req.body;
  try {
    const result = await pool.query("SELECT password FROM guestbook WHERE id = $1", [id]);
    if (result.rows.length > 0 && result.rows[0].password === password) {
      await pool.query("DELETE FROM guestbook WHERE id = $1", [id]);
      res.json({ message: "삭제되었습니다." });
    } else {
      res.status(403).json({ error: "비밀번호가 일치하지 않습니다." });
    }
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

// Like an entry
app.post("/api/guestbook/:id/like", async (req, res) => {
  const { id } = req.params;
  try {
    const result = await pool.query(
      "UPDATE guestbook SET likes = likes + 1 WHERE id = $1 RETURNING id, name, message, created_at, likes",
      [id]
    );
    if (result.rows.length > 0) {
      res.json(result.rows[0]);
    } else {
      res.status(404).json({ error: "Entry not found" });
    }
  } catch (err) {
    res.status(500).json({ error: err.message });
  }
});

const PORT = process.env.PORT || 3001;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}`);
});