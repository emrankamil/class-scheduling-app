import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

const V1_Home = () => {
    return(
      <div className="mx-auto flex flex-col items-center my-4">
        <h1 className="p-4 font-bold text-xl">Scheduling Algorithm</h1>
        <div className="flex gap-4 items-center">
          <Link to={"/v1/class"}>
            <div className="min-h-40 min-w-40 bg-gray-500 hover:bg-gray-600 rounded-lg p-2 ">
              <h1>Schedule Class</h1>
              <p>lorem epsum</p>
            </div>
          </Link>
          <Link to={"/v1/exam"}>
            <div className="min-h-40 min-w-40 bg-gray-500 hover:bg-gray-600 rounded-lg p-2">
              <h1>Schedule Exam</h1>
              <p>lorem epsum</p>
            </div>
          </Link>
        </div>
      </div>

    );
  };
  
  export default V1_Home;
  