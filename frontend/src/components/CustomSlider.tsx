import React from "react";
import Slider from "react-slick";
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";

interface SliderProps {
    children: React.ReactNode;
}

const CustomSlider: React.FC<SliderProps> = ({ children }) => {
    const settings = {
        dots: false,
        infinite: true,
        speed: 500,
        slidesToShow: 3,
        slidesToScroll: 1,
        autoplay: true,
        autoplaySpeed: 3000,
        arrows: false,
        responsive: [
            {
                breakpoint: 1024,
                settings: { slidesToShow: 2 },
            },
            {
                breakpoint: 768,
                settings: { slidesToShow: 1 },
            },
            {
                breakpoint: 480, // For very small screens
                settings: { slidesToShow: 1 },
            }
        ]
    };

    return (
        <div className="mt-5">
            <Slider {...settings}>{children}</Slider>
        </div>
    );
};

export default CustomSlider;
