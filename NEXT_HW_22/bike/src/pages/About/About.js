import React from 'react';
import styles from './About.module.css';

const About = () => {
    return (
        <div className={styles.aboutContainer}>
            <h1>About 따릉이 대여소 정보</h1>
            <p>
                따릉이 대여소 정보 사이트는 서울시의 따릉이 대여소 정보를 제공하여 사용자가 편리하게 자전거를 대여할 수 있도록 돕는 서비스입니다.
                본 사이트는 서울시의 공공데이터를 활용하여 대여소의 위치와 세부 정보를 제공합니다.
            </p>
        </div>
    );
};

export default About;
