// src/components/Main.js
import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import '../styles/styles.css';

const Main = () => {
    const [posts, setPosts] = useState([]);
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [image1, setImage1] = useState(null);
    const [image2, setImage2] = useState(null);
    const [image3, setImage3] = useState(null);

    useEffect(() => {
        localStorage.removeItem('posts'); // Clear local storage
        setPosts([]);
    }, []);

    const handleImageChange = (e, setImage) => {
        const file = e.target.files[0];
        if (file) {
            convertToBase64(file).then((base64Image) => setImage(base64Image));
        }
    };

    const handleSubmit = (e) => {
        e.preventDefault();
        const newPost = {
            title,
            content,
            images: [image1, image2, image3].filter(Boolean),
        };
        const updatedPosts = [...posts, newPost];
        setPosts(updatedPosts);
        localStorage.setItem('posts', JSON.stringify(updatedPosts));
        setTitle('');
        setContent('');
        setImage1(null);
        setImage2(null);
        setImage3(null);
    };

    const convertToBase64 = (file) => {
        return new Promise((resolve, reject) => {
            const reader = new FileReader();
            reader.readAsDataURL(file);
            reader.onloadend = () => resolve(reader.result);
            reader.onerror = reject;
        });
    };

    return (
        <div className="main-container">
            <h1>블로그</h1>
            <form onSubmit={handleSubmit} className="post-form">
                <input
                    type="text"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                    placeholder="Title"
                    required
                />
                <textarea
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                    placeholder="Content"
                    required
                ></textarea>
                <input type="file" accept="image/*" onChange={(e) => handleImageChange(e, setImage1)} required />
                <input type="file" accept="image/*" onChange={(e) => handleImageChange(e, setImage2)} required />
                <input type="file" accept="image/*" onChange={(e) => handleImageChange(e, setImage3)} required />
                <button type="submit">Add Post</button>
            </form>
            <div className="post-list">
                {posts.map((post, index) => (
                    <div key={index} className="post">
                        <h2>{post.title}</h2>
                        <p>{post.content}</p>
                        <div className="post-images">
                            {post.images.map((image, idx) => (
                                <img key={idx} src={image} alt={`Post ${index} - Image ${idx}`} />
                            ))}
                        </div>
                        <Link to={`/detail/${index}`}>Read More</Link>
                    </div>
                ))}
            </div>
        </div>
    );
};

export default Main;
