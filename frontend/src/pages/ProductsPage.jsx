// src/pages/ProductsPage.jsx
import React, { useState, useEffect } from 'react';

function ProductsPage() {
  // 1. Creamos una variable de estado para guardar la lista de productos.
  // Empieza como un array vacío [].
  const [products, setProducts] = useState([]);

  // 2. Usamos useEffect para hacer la llamada a la API cuando el componente se monta.
  useEffect(() => {
    // Definimos la función que busca los datos.
    async function fetchProducts() {
      try {
        const response = await fetch('http://localhost:8000/api/products/');
        const data = await response.json();
        setProducts(data); // 4. Guardamos los datos recibidos en nuestro estado.
      } catch (error) {
        console.error("Error al obtener los productos:", error);
      }
    }

    fetchProducts(); // 3. Ejecutamos la función.
  }, []); // El array vacío [] asegura que esto se ejecute solo una vez.

  return (
    <div>
      <h2>Gestión de Productos</h2>
      
      {/* 5. Mostramos los datos en pantalla */}
      <ul>
        {products.map(product => (
          <li key={product.id}>
            {product.name} - ${product.selling_price}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default ProductsPage;