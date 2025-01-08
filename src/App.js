import React, { useState } from "react";
import BreedList from "./components/BreedList";
import DogModal from "./components/DogModal";
import "./App.css";

const App = () => {
  const [selectedBreed, setSelectedBreed] = useState(null);
  const [modalOpen, setModalOpen] = useState(false);

  const handleSelectBreed = (breed) => {
    setSelectedBreed(breed);
    setModalOpen(true);
  };

  const closeModal = () => {
    setModalOpen(false);
  };

  return (
    <div>
      <h1>Dog Picture App</h1>
      <BreedList onSelectBreed={handleSelectBreed} />
      {modalOpen && (
        <DogModal breed={selectedBreed} isOpen={modalOpen} onClose={closeModal} />
      )}
    </div>
  );
};

export default App;
