import styled from "styled-components";

export default function Header() {
  return (
    <>
      <nav class="navbar bg-dark">
        <div class="container-fluid justify-content-center">
          <h1 class="text-white" href="#">
            Dexparser
          </h1>
        </div>

        <ul class="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
          <li>
            <a href="/list" class="nav-link px-2 text-white">
              ApkList
            </a>
          </li>
          <li>
            <a href="/dex" class="nav-link px-2 text-white">
              DexInfo
            </a>
          </li>
        </ul>
      </nav>
    </>
  );
}
