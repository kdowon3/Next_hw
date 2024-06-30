import React from 'react';
import styles from './Footer.module.css';

const Footer = () => {
    return (
        <footer className={styles.footerContainer}>
            <p>&copy; 2023 따릉이 대여소 정보</p>
            <div className={styles.footerLinks}>
                <a href="#">Privacy Policy</a>
                <a href="#">Terms of Service</a>
                <a href="#">Contact Us</a>
            </div>
        </footer>
    );
};

export default Footer;
