import React from 'react';
import './Filters.css';

const Filters = ({filters, onFilterChange, onApplyFilters}) => {
    return (
        <div className="filters-container">
            <h2>Filters</h2>
            <div className="filter-group">
                <label className="filter-label">
                    Name:
                    <input
                        type="text"
                        name="name"
                        value={filters.name}
                        onChange={onFilterChange}
                        className="filter-input"
                    />
                </label>
            </div>
            <div className="filter-group">
                <label className="filter-label">
                    Status:
                    <input
                        type="text"
                        name="status"
                        value={filters.status}
                        onChange={onFilterChange}
                        className="filter-input"
                    />
                </label>
            </div>
            <div className="filter-group">
                <label className="filter-label">
                    Employee Name:
                    <input
                        type="text"
                        name="employeeName"
                        value={filters.employeeName}
                        onChange={onFilterChange}
                        className="filter-input"
                    />
                </label>
            </div>
            <div className="filter-group">
                <label className="filter-label">
                    Request Type:
                    <select
                        name="requestType"
                        value={filters.requestType}
                        onChange={onFilterChange}
                        className="filter-input"
                    >
                        <option value="">All</option>
                        <option value="Purchase">Purchase</option>
                        <option value="Reimbursement">Reimbursement</option>
                    </select>
                </label>
            </div>
            <button onClick={onApplyFilters} className="apply-filters-button">
                Apply Filters
            </button>
        </div>
    );
};

export default Filters;
