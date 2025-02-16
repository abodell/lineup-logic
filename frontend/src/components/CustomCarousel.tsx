import React, { useState, useEffect, ReactNode } from 'react';
import { Row, Col, Container } from 'react-bootstrap';

interface ResponsiveCarouselProps {
  children: ReactNode[];
  autoplayInterval?: number;
  className?: string;
}

const CustomCarousel: React.FC<ResponsiveCarouselProps> = ({ 
  children,
  autoplayInterval = 3000,
  className = ''
}) => {
  const [visibleIndex, setVisibleIndex] = useState(0);
  const [itemsPerPage, setItemsPerPage] = useState(3);

  // Determine items per page based on screen width
  useEffect(() => {
    const handleResize = () => {
      if (window.innerWidth < 576) {
        setItemsPerPage(1);
      } else if (window.innerWidth < 992) {
        setItemsPerPage(2);
      } else {
        setItemsPerPage(3);
      }
    };

    // Set initial value
    handleResize();

    // Add event listener
    window.addEventListener('resize', handleResize);

    // Clean up
    return () => window.removeEventListener('resize', handleResize);
  }, []);

  // Auto rotation
  useEffect(() => {
    if (children.length <= itemsPerPage) return;
    
    const interval = setInterval(() => {
      setVisibleIndex((prevIndex) => 
        (prevIndex + 1) % (children.length - itemsPerPage + 1)
      );
    }, autoplayInterval);

    return () => clearInterval(interval);
  }, [children.length, itemsPerPage, autoplayInterval]);

  // Calculate visible items
  const visibleItems = children.slice(visibleIndex, visibleIndex + itemsPerPage);

  if (!children.length) return null;

  return (
    <Container fluid className={`py-3 position-relative mt-5 ${className}`}>
      <Row className="justify-content-center">
        {visibleItems.map((item, index) => (
          <Col key={index} xs={12} sm={6} lg={4} className="mb-3 d-flex justify-content-center">
            <div style={{ width: '100%', maxWidth: '16rem' }}>
              {item}
            </div>
          </Col>
        ))}
      </Row>
    </Container>
  );
};

export default CustomCarousel;