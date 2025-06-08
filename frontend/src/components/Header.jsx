// src/components/Header.jsx
import React from 'react';

function Header() {
  return (
    <header style={{ 
      backgroundColor: '#2c3e50', 
      color: 'white', 
      padding: '1rem 2rem', 
      boxShadow: '0 2px 4px rgba(0,0,0,0.1)' 
    }}>
      <h2>Nexus POS</h2>
    </header>
  );
}

export default Header;