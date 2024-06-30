import React from 'react';
import { Link } from 'react-router-dom';
import styles from './Header.module.css';

const Header = () => {
    return (
        <header className={styles.headerContainer}>
            <h1>따릉이 대여소 정보</h1>
            <nav className={styles.navLinks}>
                <Link to="/">Home</Link>
                <Link to="/bike-stations">Bike Stations</Link>
                <Link to="/about">About</Link>
            </nav>
        </header>
    );
};

export default Header;
