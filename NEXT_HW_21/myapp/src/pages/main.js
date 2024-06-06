import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import './main.css'; // Main.css 파일 import

const Main = () => {
  const [posts, setPosts] = useState([]);
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');
  const [images, setImages] = useState([]);

  useEffect(() => {
    const storedPosts = JSON.parse(localStorage.getItem('posts')) || [];
    setPosts(storedPosts);
  }, []);

  const AddPost = (e) => {
    e.preventDefault();
    const newPost = { title, content, images };
    const updatedPosts = [...posts, newPost];
    setPosts(updatedPosts);
    localStorage.setItem('posts', JSON.stringify(updatedPosts));
    setTitle('');
    setContent('');
    setImages([]);
  };

  const ImageChange = (e) => {
    const files = Array.from(e.target.files);
    setImages(files.map(file => URL.createObjectURL(file)));
  };

  return (
    <div className="container">
      <div className="main-content">
        <h1>Main Page</h1>
        <form onSubmit={AddPost}>
          <input 
            type="text" 
            placeholder="Title" 
            value={title} 
            onChange={(e) => setTitle(e.target.value)} 
            required 
          />
          <textarea 
            placeholder="Content" 
            value={content} 
            onChange={(e) => setContent(e.target.value)} 
            required 
          />
          <input 
            type="file" 
            accept="image/*" 
            multiple 
            onChange={ImageChange} 
          />
          <button type="submit">Add Post</button>
        </form>
        {posts.map((post, index) => (
          <div key={index} className="post">
            <h2 className="post-title">{post.title} <Link to={`/detail/${index}`}>Read More</Link></h2>
            <div>
              {post.images.map((img, i) => (
                <img key={i} src={img} alt={`Post ${index} - ${i}`} />
              ))}
            </div>
            <p className="post-content">{post.content}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default Main;
