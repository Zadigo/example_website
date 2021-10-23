<template>
  <b-navbar
    id="main-navbar"
    class="navbar navbar-expand-lg navbar-light bg-white fixed-top"
  >
    <div class="container-fluid">
      <!-- Toggle button -->
      <b-btn
        class="navbar-toggler"
        @click="$emit('toggleSidebar')"
      >
        <font-awesome-icon icon="bars" />
      </b-btn>
      
      <!-- <button class="navbar-toggler" type="button" data-mdb-toggle="collapse" data-mdb-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation" >
        <font-awesome-icon icon="bars"></font-awesome-icon>
      </button> -->

      <!-- Brand -->
      <a
        class="navbar-brand"
        href="#"
      >
        <!-- <img src="https://mdbootstrap.com/img/logo/mdb-transaprent-noshadows.png" height="25" alt="" loading="lazy" /> -->
        <b-img
          height="25"
          src="https://mdbootstrap.com/img/logo/mdb-transaprent-noshadows.png"
        />
      </a>

      <!-- Search form -->
      <!-- <form class="d-none d-md-flex input-group w-auto my-auto">
        <input autocomplete="off" type="search" class="form-control rounded" placeholder='Search' style="min-width: 225px" />
        <span class="input-group-text border-0">
          <font-awesome-icon icon="search"></font-awesome-icon>
        </span>
      </form> -->

      <b-form class="d-none d-md-flex input-group w-auto my-auto">
        <b-input
          autocomplete="off"
          class="form-control rounded"
          placeholder="Search"
          style="min-width: 225px;"
          type="search"
        />
        <span class="input-group-text border-0">
          <font-awesome-icon icon="search" />
        </span>
      </b-form>

      <!-- Right links -->
      <!-- <b-navbar-nav class="navbar-nav ms-auto d-flex flex-row">        
        <b-link class="nav-link me-3 me-lg-0 dropdown-toggle hidden-arrow" id="navbarDropdownMenuLink" role="button" data-mdb-toggle="dropdown" aria-expanded="false">
          <font-awesome-icon icon="bell"></font-awesome-icon>
          <span class="badge rounded-pill badge-notification bg-danger">1</span>
        </b-link>

        <b-nav-item-dropdown>
          <b-dropdown-item href="#">Some news</b-dropdown-item>
          <b-dropdown-item href="#">Something else</b-dropdown-item>
          <b-dropdown-item href="#">Another news</b-dropdown-item>
        </b-nav-item-dropdown>
      </b-navbar-nav> -->

      <ul class="navbar-nav ms-auto d-flex flex-row">        
        <!-- Notification dropdown -->
        <li class="nav-item dropdown">
          <a
            id="navbarDropdownMenuLink"
            aria-expanded="false"
            class="nav-link me-3 me-lg-0 dropdown-toggle hidden-arrow"
            data-mdb-toggle="dropdown"
            href="#"
            role="button"
          >
            <font-awesome-icon icon="bell" />
            <span class="badge rounded-pill badge-notification bg-danger">1</span>
          </a>

          <ul
            aria-labelledby="navbarDropdownMenuLink"
            class="dropdown-menu dropdown-menu-end"
          >
            <li>
              <a
                class="dropdown-item"
                href="#"
              >Some news</a>
            </li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              >Another news</a>
            </li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              >Something else here</a>
            </li>
          </ul>
        </li>

        <!-- Icon -->
        <li class="nav-item">
          <a
            class="nav-link me-3 me-lg-0"
            href="#"
          >
            <font-awesome-icon icon="fill-drip" />
          </a>
        </li>

        <!-- Icon -->
        <li class="nav-item me-3 me-lg-0">
          <a
            class="nav-link"
            href="#"
          >
            <i class="fab fa-github" />
          </a>
        </li>

        <!-- Icon dropdown -->
        <li class="nav-item dropdown">
          <a
            id="navbarDropdown"
            aria-expanded="false"
            class="nav-link me-3 me-lg-0 dropdown-toggle hidden-arrow"
            data-mdb-toggle="dropdown"
            href="#"
            role="button"
          >
            <i class="united kingdom flag m-0" />
          </a>
          <ul
            aria-labelledby="navbarDropdown"
            class="dropdown-menu dropdown-menu-end"
          >
            <li>
              <a
                class="dropdown-item"
                href="#"
              >
                <i class="united kingdom flag" />English
                <i class="fa fa-check text-success ms-2" />
              </a>
            </li>
            <li><hr class="dropdown-divider"></li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              ><i class="poland flag" />Polski</a>
            </li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              ><i class="china flag" />中文</a>
            </li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              ><i class="japan flag" />日本語</a>
            </li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              ><i class="germany flag" />Deutsch</a>
            </li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              ><i class="france flag" />Français</a>
            </li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              ><i class="spain flag" />Español</a>
            </li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              ><i class="russia flag" />Русский</a>
            </li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              ><i class="portugal flag" />Português</a>
            </li>
          </ul>
        </li>

        <!-- Avatar -->
        <li class="nav-item dropdown">
          <a
            id="navbarDropdownMenuLink"
            aria-expanded="false"
            class="nav-link dropdown-toggle hidden-arrow d-flex align-items-center"
            data-mdb-toggle="dropdown"
            href="#"
            role="button"
          >
            <img
              alt=""
              class="rounded-circle"
              height="22"
              loading="lazy"
              src="https://mdbootstrap.com/img/Photos/Avatars/img (31).jpg"
            >
          </a>
          <ul
            aria-labelledby="navbarDropdownMenuLink"
            class="dropdown-menu dropdown-menu-end"
          >
            <li>
              <a
                class="dropdown-item"
                href="#"
              >My profile</a>
            </li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              >Settings</a>
            </li>
            <li>
              <a
                class="dropdown-item"
                href="#"
              >Logout</a>
            </li>
          </ul>
        </li>
      </ul>
    </div>
    <!-- Container wrapper -->
  </b-navbar>
</template>

<script>
export default {
  name: 'BaseNavbar'
}
</script>
