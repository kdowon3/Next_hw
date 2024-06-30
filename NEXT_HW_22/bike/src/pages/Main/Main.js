import React from 'react';
import styles from './Main.module.css';

const Main = () => {
    return (
        <div className={styles.mainContainer}>
            <h1>Welcome to 따릉이 대여소 정보</h1>
            <p>서울시의 따릉이 대여소 정보를 제공하여 사용자가 편리하게 자전거를 대여할 수 있도록 돕는 서비스입니다.</p>
            <a href="/bike-stations">대여소 정보 확인하기</a>
        </div>
    );
};

export default Main;
