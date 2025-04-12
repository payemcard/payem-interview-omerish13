import React, {useEffect, useState} from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import { HOST_WITH_PORT } from '../consts';
import './ShowRequests.css';
import Filters from './Filters';
import { IoMdHome } from "react-icons/io";
import { IoCheckmarkCircle } from "react-icons/io5";
import { IoIosCloseCircle } from "react-icons/io";
import { MdPending } from "react-icons/md";


const ShowRequests = () => {
    const [requests, setRequests] = useState([]);
    const [filteredRequests, setFilteredRequests] = useState([]);
    const [responseMessage, setResponseMessage] = useState(null);
    const [filters, setFilters] = useState({
        name: '',
        status: '',
        employeeName: '',
    });
    const navigate = useNavigate();

    const fetchRequests = async () => {
        try {
            const response = await axios.get(`${HOST_WITH_PORT}/api/requests`);
            setRequests(response.data);
            setFilteredRequests(response.data);
            setResponseMessage({ type: 'success', text: 'Requests Fetched Successfully!' });
            setTimeout(() => setResponseMessage(null), 3000);
        } catch (error) {
            setResponseMessage({ type: 'error', text: 'Error Fetching Requests' });
            setTimeout(() => setResponseMessage(null), 3000);
            console.error('Error fetching requests', error);
        }
    };

    const handleFilterChange = (e) => {
        setFilters({
            ...filters,
            [e.target.name]: e.target.value,
        });
    };

    function includesIgnoreCase(source = '', target = '') {
        return source.toLowerCase().includes(target.toLowerCase());
    }


    const handleApplyFilters = () => {
        const filteredRequests = requests.filter((request) => {
            return (
              (filters.name ? includesIgnoreCase(request.name, filters.name) : true) &&
              (filters.status ? includesIgnoreCase(request.status, filters.status) : true) &&
              (filters.employeeName ? includesIgnoreCase(request.employee_name, filters.employeeName) : true)
            );
        });
        // change the state of requests to the filtered requests temporarily
        setFilteredRequests(filteredRequests);
    }

    const handleRowClick = (id) => {
        navigate(`/requests/${id}`);
    };

    const handleStatusIcons = (status) => {
        switch (status) {
            case 'Approved':
                return <IoCheckmarkCircle className="approve-icon"/>;
            case 'Declined':
                return <IoIosCloseCircle className="decline-icon"/> ;
            case 'Pending':
                return <MdPending className="pending-icon"/>;
            default:
                return null;
        }
    }

    useEffect(() => {
        fetchRequests();

    },[]);
    return (
        <div className="requests-container">
            <button onClick={() => navigate('/')} className="back-button"><IoMdHome /></button>
            <h1>Show Requests</h1>
            <Filters filters={filters} onFilterChange={handleFilterChange} onApplyFilters={handleApplyFilters} />
            <button onClick={fetchRequests} className="fetch-button">Fetch Requests</button>
            <table className="requests-table">
                <thead>
                    <tr>
                        <th>Request ID</th>
                        <th>Name</th>
                        <th>Description</th>
                        <th>Amount</th>
                        <th>Currency</th>
                        <th>Employee Name</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
                    {filteredRequests.map((request) => (
                        <tr
                            key={request.id}
                            onClick={() => handleRowClick(request.id)}
                            className="clickable-row"
                        >
                            <td>{request.id}</td>
                            <td>{request.name}</td>
                            <td>{request.description}</td>
                            <td>{request.amount}</td>
                            <td>{request.currency}</td>
                            <td>{request.employee_name}</td>
                            <td>{handleStatusIcons(request.status)}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
            {responseMessage && (
                <div className={`snackbar ${responseMessage.type} show`}>
                    {responseMessage.text}
                </div>
            )}
        </div>
    );
};

export default ShowRequests;
