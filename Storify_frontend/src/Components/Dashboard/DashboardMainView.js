import React, { useEffect } from 'react';
import {
  Routes,
  Route,
  useLocation
} from 'react-router-dom';

import './css/style.css';
// import './ch'
import './charts/ChartjsConfig';

// Import pages
import DashboardHome from './pages/DashboardHome';

function DashboardMainView() {

  const location = useLocation();

  useEffect(() => {
    document.querySelector('html').style.scrollBehavior = 'auto'
    window.scroll({ top: 0 })
    document.querySelector('html').style.scrollBehavior = ''
  }, [location.pathname]); // triggered on route change

  return (
    <>
      <Routes>
        <Route exact path="/" element={<DashboardHome />} />
      </Routes>
    </>
  );
}

export default DashboardMainView;
