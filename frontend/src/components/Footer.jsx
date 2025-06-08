// src/components/Footer.jsx
import React from 'react';

function Footer() {
  const currentYear = new Date().getFullYear();
  return (
    <footer style={{ 
      backgroundColor: '#ecf0f1', 
      color: '#34495e',
      padding: '1rem', 
      textAlign: 'center', 
      position: 'fixed', 
      bottom: 0, 
      width: '100%' 
    }}>
      <p style={{ margin: 0 }}>
        &copy; {currentYear} Nexus POS - Desarrollado por Matías y Nexus.
      </p>
    </footer>
  );
}

export default Footer;