import React from 'react';
import { Route, Routes, Link } from 'react-router-dom';
import Main from './pages/main';
import Detail from './pages/detail';


function App() {
  return (
    <div>
      <nav>
        <Link to="/">main으로 가기</Link>
      </nav>
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/detail/:id" element={<Detail />} />
      </Routes>
    </div>
  );
}

export default App;
