// src/App.jsx
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import Header from './components/Header';
import Footer from './components/Footer';

// Importamos nuestras páginas
import PosPage from './pages/PosPage';
import ProductsPage from './pages/ProductsPage';
import SalesPage from './pages/SalesPage';


function App() {
  return (
    <BrowserRouter>
      <div style={{ display: 'flex', flexDirection: 'column', minHeight: '100vh' }}>
        <Header />
        
        {/* Links de Navegación de ejemplo, podrían ir en el Header más adelante */}
        <nav style={{ padding: '1rem', background: '#f4f4f4' }}>
          <Link to="/" style={{ marginRight: '1rem' }}>Punto de Venta</Link>
          <Link to="/products" style={{ marginRight: '1rem' }}>Productos</Link>
          <Link to="/sales">Ventas</Link>
        </nav>

        <main style={{ flex: 1, padding: '2rem' }}>
          <Routes>
            <Route path="/" element={<PosPage />} />
            <Route path="/products" element={<ProductsPage />} />
            <Route path="/sales" element={<SalesPage />} />
            {/* Aquí añadiremos más rutas en el futuro, como la de reportes */}
          </Routes>
        </main>

        <Footer />
      </div>
    </BrowserRouter>
  )
}

export default App;