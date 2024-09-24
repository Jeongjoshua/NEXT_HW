import ProductList from './component/ProductList'
import Cart from './component/Cart'

export default function Home() {
  return (
    <main style={{ padding: '2rem' }}>
      <h1>Next.js Shopping Cart with Context API</h1>
      <div style={{ display: 'flex', gap: '2rem', flexWrap: 'wrap' }}>
        <div style={{ flex: 2 }}>
          <ProductList />
        </div>
        <div style={{ flex: 1 }}>
          <Cart />
        </div>
      </div>
    </main>
  )
}