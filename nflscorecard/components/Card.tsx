// components/Card.tsx

import React from 'react';

interface CardProps {
  children: React.ReactNode;
}

const Card: React.FC<CardProps> = () => {
  return (
    <div className="bg-white rounded-card shadow-card p-6">
        <h3>test</h3>
    </div>
  );
};

export default Card;
