import React, { useState } from 'react';
import './App.css';

import { BrowserRouter, Routes, Route } from "react-router-dom";

// import Login from "./pages/v1/Login"
// import Layout from './pages/v1/Layout';
// import V1_Home from './pages/v1/Home';
// import NoPage from './pages/v1/NoPage';
// import SignUp from './pages/v1/SignUp';
import Schedule_class from './pages/v1/Schedule_class'

// import V2_Home from './pages/v2/Home';
// import Landing from './pages/Landing';

function App() {

  //const [isLoggedIn, setIsLoggedIn] = useState(false);
  
  return (
    <BrowserRouter>
      <Routes>
        {/* <Route path='/v1' element={<Layout/>}>
        <Route index element={<V1_Home/>} />
          <Route path='/v1/class' element={<Schedule_class/>} />
        </Route>

        <Route path="/v2" element={<Layout/>}>      
          <Route index element={<V2_Home />} />
        </Route>

        <Route path="*" element={<NoPage />} />
        <Route path="/" element={<Landing/>} />
        <Route path="/login" element={<Login/>} />
        <Route path='/signup' element={<SignUp/>}/> */}

        <Route path='/class' element={<Schedule_class/>}/>

      </Routes>
    </BrowserRouter>
  );
}

export default App;
