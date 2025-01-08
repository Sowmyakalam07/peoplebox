import React, { useEffect, useState } from "react";
import Modal from "react-modal";
import axios from "axios";

Modal.setAppElement("#root");

const DogModal = ({ breed, isOpen, onClose }) => {
  const [images, setImages] = useState([]);

  useEffect(() => {
    if (breed) {
      axios
        .get(`https://dog.ceo/api/breed/${breed}/images/random/4`)
        .then((response) => {
          setImages(response.data.message);
        });
    }
  }, [breed]);

  return (
    <Modal isOpen={isOpen} onRequestClose={onClose}>
      <button onClick={onClose}>Close</button>
      <div>
        {images.map((img, index) => (
          <img key={index} src={img} alt={breed} style={{ width: "100px" }} />
        ))}
      </div>
    </Modal>
  );
};

export default DogModal;
