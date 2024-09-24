'use client';  // Add this line at the top of the file

import { useCart } from '../../context/CartContext';

const products = [
  { id: 1, name: 'T-Shirt', price: 15.99 },
  { id: 2, name: 'Jeans', price: 39.99 },
  { id: 3, name: 'Sneakers', price: 59.99 },
];

export default function ProductList() {
  const { addToCart } = useCart();

  return (
    <div>
      <h2>Products</h2>
      {products.map((product) => (
        <div key={product.id} style={{ marginBottom: '1rem' }}>
          <h3>{product.name}</h3>
          <p>Price: ${product.price.toFixed(2)}</p>
          <button onClick={() => addToCart(product)}>Add to Cart</button>
        </div>
      ))}
    </div>
  );
}