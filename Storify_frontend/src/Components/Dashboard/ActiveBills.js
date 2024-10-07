import React, { useEffect, useState, useContext } from "react";
import axios from "axios";
import AuthContext from "../../context/AuthContext"; // Adjust path as necessary

function ActiveBills() {
    const [bills, setBills] = useState([]);
    const { user } = useContext(AuthContext);

    useEffect(() => {
        const fetchBills = async () => {
            if (!user || !user.id) {
                console.error("User is not authenticated.");
                return; // Exit if user is not authenticated
            }
        
            try {
                const token = localStorage.getItem("authTokens");
                const response = await axios.get(`http://127.0.0.1:8000/api/bills/?user=${user.id}`, {
                    headers: {
                        'Authorization': `Bearer ${token}`,
                    },
                });
                setBills(response.data);
            } catch (error) {
                console.error("Error fetching bills:", error);
            }
        };
        

        fetchBills();
    }, [user.id]);

    return (
        <div className="p-6 bg-gradient-to-br from-blue-50 to-blue-100 min-h-screen">
            <h1 className="text-3xl font-bold text-blue-700 mb-4">Active Bills</h1>
            <table className="min-w-full bg-white border-collapse border border-gray-300">
                <thead>
                    <tr className="bg-gray-100">
                        <th className="border border-gray-300 p-3 text-left">Bill Number</th>
                        <th className="border border-gray-300 p-3 text-left">Vendor</th>
                        <th className="border border-gray-300 p-3 text-left">Total Amount</th>
                        <th className="border border-gray-300 p-3 text-left">Due Date</th>
                    </tr>
                </thead>
                <tbody>
                    {bills.map((bill) => (
                        <tr key={bill.id}>
                            <td className="border border-gray-300 p-3">{bill.billNumber}</td>
                            <td className="border border-gray-300 p-3">{bill.vendor}</td>
                            <td className="border border-gray-300 p-3">${bill.totalAmount}</td>
                            <td className="border border-gray-300 p-3">{new Date(bill.dueDate).toLocaleDateString()}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default ActiveBills;
