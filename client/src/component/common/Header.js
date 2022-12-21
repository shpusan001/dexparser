import { Link } from "react-router-dom";
import styled from "styled-components";

export default function Header() {
  return (
    <>
      <nav class="navbar bg-dark">
        <div class="container-fluid justify-content-center">
          <h1 class="text-white" href="#">
            Dex parser
          </h1>
        </div>

        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li>
            <Link to={"/list"} className="nav-link px-2 text-white">
              ApkList
            </Link>
          </li>
          <li>
            <Link to={"/dex"} className="nav-link px-2 text-white">
              DexInfo
            </Link>
          </li>
          <li>
            <Link to={"/setting"} className="nav-link px-2 text-white">
              Setting
            </Link>
          </li>
        </ul>
      </nav>
    </>
  );
}
