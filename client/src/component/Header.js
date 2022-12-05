import styled from "styled-components";

export default function Header() {
  return (
    <>
      <div class="page-header bg-primary">
        <div class="jumbotron text-center">
          <h1 class="text-white">Dex parser</h1>
        </div>
      </div>

      <ul class="nav nav-pills justify-content-center nav-fill">
        <li class="nav-item">
          <a
            class="nav-link active"
            id="pills-home-tab"
            data-toggle="pill"
            role="tab"
            aria-controls="pills-home"
            aria-selected="true"
          >
            ApkList
          </a>
        </li>
        q
        <li class="nav-item">
          <a
            class="nav-link"
            id="pills-profile-tab"
            data-toggle="pill"
            role="tab"
            aria-controls="pills-profile"
            aria-selected="false"
          >
            DexInfo
          </a>
        </li>
      </ul>
    </>
  );
}
