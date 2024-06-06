import React, { useEffect, useState, useRef } from 'react';
import { useParams, useNavigate, Link } from 'react-router-dom';
import './detail.css';

const Detail = () => {
  const { id } = useParams();
  const [post, setPost] = useState(null);
  const [comment, setComment] = useState('');
  const [comments, setComments] = useState([]);
  const imageRefs = useRef([]);
  const navigate = useNavigate();

  useEffect(() => {
    const storedPosts = JSON.parse(localStorage.getItem('posts')) || [];
    setPost(storedPosts[id]);
    setComments(storedPosts[id].comments || []);
  }, [id]);

  const DeletePost = () => {
    const storedPosts = JSON.parse(localStorage.getItem('posts')) || [];
    const updatedPosts = storedPosts.filter((_, index) => index !== parseInt(id));
    localStorage.setItem('posts', JSON.stringify(updatedPosts));
    navigate('/');
  };

  const AddComment = () => {
    if (!comment.trim()) return;
    const newComment = {
      id: comments.length + 1,
      content: comment.trim(),
    };
    const updatedComments = [...comments, newComment];
    setComments(updatedComments);
    setComment('');
    const storedPosts = JSON.parse(localStorage.getItem('posts')) || [];
    storedPosts[id].comments = updatedComments;
    localStorage.setItem('posts', JSON.stringify(storedPosts));
  };

  const DeleteComment = (commentId) => {
    const updatedComments = comments.filter(comment => comment.id !== commentId);
    setComments(updatedComments);
    const storedPosts = JSON.parse(localStorage.getItem('posts')) || [];
    storedPosts[id].comments = updatedComments;
    localStorage.setItem('posts', JSON.stringify(storedPosts));
  };

  return (
    <div className="container">
      <div className="main-content">
        {post && (
          <>
            <h1>{post.title}</h1>
            <div>
              {post.images.map((img, index) => (
                <img key={index} src={img} alt={`Post image ${index}`} ref={el => imageRefs.current[index] = el} />
              ))}
            </div>
            <p>{post.content}</p>
            <button onClick={DeletePost}>Delete Post</button>
            <div className="comment-section">
              <h3>Comments</h3>
              <input 
                type="text" 
                value={comment} 
                onChange={(e) => setComment(e.target.value)} 
                placeholder="Add a comment"
              />
              <button onClick={AddComment}>Add Comment</button>
              <div>
                {comments.map(comment => (
                  <div key={comment.id}>
                    <p>{comment.content}</p>
                    <button onClick={() => DeleteComment(comment.id)}>Delete Comment</button>
                  </div>
                ))}
              </div>
            </div>
          </>
        )}
      </div>
    </div>
  );
};

export default Detail;
