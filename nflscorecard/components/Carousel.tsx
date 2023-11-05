'use client'
import React from 'react';
import Slider from 'react-slick';
const Carousel = () => {
  const settings = {
    dots: true,
    infinite: true,
    speed: 500,
    slidesToShow: 1,
    slidesToScroll: 1,
  };

  return (
    <Slider {...settings}>
      <div>
        <h2>Slide 1</h2>
      </div>
      <div>
        <h2>Slide 2</h2>
      </div>
      <div>
        <h2>Slide 3</h2>
      </div>
      {/* Add more slides as needed */}
    </Slider>
  );
};

export default Carousel;