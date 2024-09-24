import ProductList from '../components/ProductList';
import Cart from '../components/Cart';

export default function Home() {
  return (
    <div style={{ padding: '2rem' }}>
      <h1>My Shop</h1>
      <div style={{ display: 'flex', justifyContent: 'space-between' }}>
        <ProductList />
        <Cart />
      </div>
    </div>
  );
}