import React, { useState, useEffect } from 'react';
import './Stations.module.css';

const BikeStations = () => {
    const [stations, setStations] = useState([]);
    const [selectedStation, setSelectedStation] = useState(null);

    useEffect(() => {
        fetch('/station.json')
            .then(response => response.json())
            .then(data => setStations(data.DATA))
            .catch(error => console.error('Error fetching the bike stations:', error));
    }, []);

    const handleStationChange = (event) => {
        const stationId = event.target.value;
        const station = stations.find(station => station.lendplace_id === stationId);
        setSelectedStation(station);
    };

    return (
        <div className="stations-container">
            <h1>서울시 따릉이 대여소 정보</h1>
            <div className="stations-dropdown">
                <select onChange={handleStationChange}>
                    <option value="">대여소를 선택하세요</option>
                    {stations.map(station => (
                        <option key={station.lendplace_id} value={station.lendplace_id}>
                            {station.statn_addr1}
                        </option>
                    ))}
                </select>
            </div>
            {selectedStation && (
                <div className="station-info">
                    <h2>{selectedStation.statn_addr1}</h2>
                    <p>상세 주소: {selectedStation.statn_addr2}</p>
                    <p>위도: {selectedStation.statn_lat}</p>
                    <p>경도: {selectedStation.statn_lnt}</p>
                </div>
            )}
        </div>
    );
};

export default BikeStations;
