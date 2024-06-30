import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Header from './components/Header/Header';
import Main from './pages/Main/Main';
import BikeStations from './components/Stations/stations'; // 경로 확인
import About from './pages/About/About';
import Footer from './components/Footer/Footer';
import './App.css';

function App() {
  return (
    <Router>
      <div>
        <Header />
        <Routes>
          <Route path="/" element={<Main />} />
          <Route path="/bike-stations" element={<BikeStations />} />
          <Route path="/about" element={<About />} />
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
