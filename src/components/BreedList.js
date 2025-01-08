import React, { useState, useEffect } from "react";
import axios from "axios";

const BreedList = ({ onSelectBreed }) => {
  const [breeds, setBreeds] = useState({});

  useEffect(() => {
    axios.get("https://dog.ceo/api/breeds/list/all").then((response) => {
      setBreeds(response.data.message);
    });
  }, []);

  return (
    <ul>
      {Object.entries(breeds).map(([breed, subBreeds]) => (
        <React.Fragment key={breed}>
          <li onClick={() => onSelectBreed(breed)}>{breed}</li>
          {subBreeds.map((subBreed) => (
            <li
              key={subBreed}
              onClick={() => onSelectBreed(`${breed}/${subBreed}`)}
              style={{ paddingLeft: "20px" }}
            >
              {subBreed}
            </li>
          ))}
        </React.Fragment>
      ))}
    </ul>
  );
};

export default BreedList;
