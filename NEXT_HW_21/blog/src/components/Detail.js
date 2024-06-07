// src/Detail.js
import React, { useEffect, useState, useRef } from 'react';
import { useParams } from 'react-router-dom';

const Detail = () => {
    const { id } = useParams();
    const [post, setPost] = useState(null);
    const imageRef = useRef(null);

    useEffect(() => {
        const savedPosts = JSON.parse(localStorage.getItem('posts')) || [];
        setPost(savedPosts[id]);
    }, [id]);

    const handleImageClick = (src) => {
        if (imageRef.current) {
            imageRef.current.href = src;
        }
    };

    if (!post) {
        return <div>Loading...</div>;
    }

    return (
        <div>
            <h1>{post.title}</h1>
            <p>{post.content}</p>
            {post.images.map((image, index) => (
                <a key={index} href={image} ref={imageRef}>
                    <img src={image} alt={`Detail ${index}`} onClick={() => handleImageClick(image)} />
                </a>
            ))}
        </div>
    );
};

export default Detail;
