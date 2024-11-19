// App.js
// import { useState } from 'react';
// import Layout from './components/Layout';
import HomePage from './pages/HomePage';
import AboutPage from './pages/AboutPage';
import ContactPage from './pages/ContactPage';

import React from 'react';
import {BrowserRouter as Router, Route, Routes, Link } from 'react-router-dom';

function App() {

  // const [page, setPage] = useState('home');

  // TODO: How doe sthe Layout component know which page to render?

  return (
    // <Layout selectedPage={page} onSetPage={setPage}>

    //   {page === 'home' && <HomePage />}
    //   {page === 'about' && <AboutPage />}
    //   {page === 'contact' && <ContactPage />}

    // </Layout>
  <Router>
    <div>
      <nav>
        <ul>
          <li>
            <Link to="/">Home</Link>
          </li>
          <li>
            <Link to="/about">About</Link>
          </li>
          <li>
            <Link to="/contact">Contact</Link>
          </li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/about" element={<AboutPage />} />
        <Route path="/contact" element={<ContactPage />} />
      </Routes>
    </div>
  </Router>
  );


}

export default App;
