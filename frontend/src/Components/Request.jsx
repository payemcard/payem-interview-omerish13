import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams } from 'react-router-dom';
import { HOST_WITH_PORT } from '../consts';
import './Requests.css';
import { IoListCircle } from "react-icons/io5";

const Request = () => {
  const { id } = useParams();
  const [request, setRequest] = useState(null);
  const [responseMessage, setResponseMessage] = useState(null);

  useEffect(() => {
    const fetchRequest = async () => {
      try {
        const response = await axios.get(`${HOST_WITH_PORT}/api/requests/${id}`);
        setRequest(response.data);
      } catch (error) {
        setResponseMessage({ type: 'error', text: 'Error Fetching Request' });
        setTimeout(() => setResponseMessage(null), 3000);
        console.error('Error fetching request', error);
      }
    };

    fetchRequest();
  }, [id]);

  // approveRequest function
    const approveRequest = async () => {
        try {
            // open a dialog to confirm the action and get the approved amount
            const approvedAmount = prompt("Enter the approved amount:");
            if (approvedAmount === null) {
                // User cancelled the prompt
                return;
            }
            if (isNaN(approvedAmount) || parseFloat(approvedAmount) <= 0) {
                alert("Please enter a valid amount.");
                return;
            }
            // send the approved amount to the server
            const requestData = {
                ...request,
                approved_amount: parseFloat(approvedAmount),
            };

            const response = await axios.put(`${HOST_WITH_PORT}/api/requests/${id}/approve`,
                requestData);
            // reload the request data
            setRequest(response.data);
            return response.data;
        } catch (error) {
            console.error('Error approving request', error);
            throw error;
        }
    }

    // declineRequest function
    const declineRequest = async () => {
        try {
            const response = await axios.put(`${HOST_WITH_PORT}/api/requests/${id}/decline`);
            // reload the request data
            setRequest(response.data);
            return response.data;
        } catch (error) {
            console.error('Error declining request', error);
            throw error;
        }
    }

    // backToResults function
    const backToResults = () => {
        // redirect to the results page
        window.location.href = '/show-requests';
    }

  if (!request) {
    return <div>Loading...</div>;
  }

  return (
    <div className="single-request-container">
        <button onClick={backToResults} className="back-button"><IoListCircle /></button>
      <h1>Request Details</h1>
      <form className="single-request-form">
        <div>
          <label>ID:</label>
          <input type="text" value={request.id} readOnly />
        </div>
        <div>
          <label>Name:</label>
          <input type="text" value={request.name} readOnly />
        </div>
        <div>
          <label>Description:</label>
          <textarea value={request.description} readOnly />
        </div>
        <div>
          <label>Amount:</label>
          <input type="number" value={request.amount} readOnly />
        </div>
        <div>
          <label>Currency:</label>
          <input type="text" value={request.currency} readOnly />
        </div>
        <div>
          <label>Employee Name:</label>
          <input type="text" value={request.employee_name} readOnly />
        </div>
        <div>
          <label>Status:</label>
          <input type="text" value={request.status} readOnly />
        </div>
      </form>
      <div className="button-group">
        <button className="approve-button" onClick={approveRequest}>Approve</button>
        <button className="decline-button" onClick={declineRequest}>Decline</button>
      </div>
      {responseMessage && (
        <div className={`snackbar ${responseMessage.type}`}>
          {responseMessage.text}
        </div>
      )}
    </div>
  );
};


export default Request;
