import React from 'react';
import { Container } from 'react-bootstrap';
import '../styles/HomePage.css'; 

const HomePage = () => {
  return (
    <div className="home-container">
      <div className="video-container">
        <video autoPlay muted>
          <source src="/assets/intro.mp4" type="video/mp4" />
          Your browser does not support the video tag.
        </video>
      </div>
      <div className="other-content">
        <img src="/assets/logo-hm.jpg" className='icon-home'></img>
        {/* Add more content as needed */}
      </div>
    </div>
  );
};

export default HomePage;
