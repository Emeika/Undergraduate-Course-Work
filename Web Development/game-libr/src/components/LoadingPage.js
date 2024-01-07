// src/components/LoadingPage.js
import React from 'react';
import '../styles/LoadingPage.css';

const LoadingPage = () => {
    return (
        <div className="loading-container">
            <div className="middle-image">
                <img src="/assets/middle.png" alt="throne" />
                <div className="overlay-image">
                    <img src="/assets/overlay.png" alt="sign" />
                </div>
            </div>
            <img src="/assets/smoke.png" alt="smoke" className="smoke-animation" />
        </div>
    );
};

export default LoadingPage;
