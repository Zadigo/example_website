<template>
  <b-navbar id="main-navbar" class="navbar navbar-expand-lg navbar-light bg-white fixed-top" >
    <div class="container-fluid">

      <!-- Toggle button -->
      <b-btn @click="$emit('toggleSidebar')" class="navbar-toggler">
        <font-awesome-icon icon="bars"></font-awesome-icon>
      </b-btn>
      
      <!-- <button class="navbar-toggler" type="button" data-mdb-toggle="collapse" data-mdb-target="#sidebarMenu" aria-controls="sidebarMenu" aria-expanded="false" aria-label="Toggle navigation" >
        <font-awesome-icon icon="bars"></font-awesome-icon>
      </button> -->

      <!-- Brand -->
      <a class="navbar-brand" href="#">
        <!-- <img src="https://mdbootstrap.com/img/logo/mdb-transaprent-noshadows.png" height="25" alt="" loading="lazy" /> -->
        <b-img src="https://mdbootstrap.com/img/logo/mdb-transaprent-noshadows.png" height="25"></b-img>
      </a>

      <!-- Search form -->
      <!-- <form class="d-none d-md-flex input-group w-auto my-auto">
        <input autocomplete="off" type="search" class="form-control rounded" placeholder='Search' style="min-width: 225px" />
        <span class="input-group-text border-0">
          <font-awesome-icon icon="search"></font-awesome-icon>
        </span>
      </form> -->

      <b-form class="d-none d-md-flex input-group w-auto my-auto">
        <b-input autocomplete="off" type="search" class="form-control rounded" placeholder="Search" style="min-width: 225px;"></b-input>
        <span class="input-group-text border-0">
          <font-awesome-icon icon="search"></font-awesome-icon>
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
          <a class="nav-link me-3 me-lg-0 dropdown-toggle hidden-arrow" href="#" id="navbarDropdownMenuLink" role="button" data-mdb-toggle="dropdown" aria-expanded="false">
            <font-awesome-icon icon="bell"></font-awesome-icon>
            <span class="badge rounded-pill badge-notification bg-danger">1</span>
          </a>

          <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdownMenuLink">
            <li><a class="dropdown-item" href="#">Some news</a></li>
            <li><a class="dropdown-item" href="#">Another news</a></li>
            <li>
              <a class="dropdown-item" href="#">Something else here</a>
            </li>
          </ul>
        </li>

        <!-- Icon -->
        <li class="nav-item">
          <a class="nav-link me-3 me-lg-0" href="#">
            <font-awesome-icon icon="fill-drip"></font-awesome-icon>
          </a>
        </li>

        <!-- Icon -->
        <li class="nav-item me-3 me-lg-0">
          <a class="nav-link" href="#">
            <i class="fab fa-github"></i>
          </a>
        </li>

        <!-- Icon dropdown -->
        <li class="nav-item dropdown">
          <a class="nav-link me-3 me-lg-0 dropdown-toggle hidden-arrow" href="#" id="navbarDropdown" role="button" data-mdb-toggle="dropdown" aria-expanded="false">
            <i class="united kingdom flag m-0"></i>
          </a>
          <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdown">
            <li>
              <a class="dropdown-item" href="#">
                <i class="united kingdom flag"></i>English
                <i class="fa fa-check text-success ms-2"></i>
              </a>
            </li>
            <li><hr class="dropdown-divider" /></li>
            <li>
              <a class="dropdown-item" href="#"
                ><i class="poland flag"></i>Polski</a
                >
            </li>
            <li>
              <a class="dropdown-item" href="#"
                ><i class="china flag"></i>中文</a
                >
            </li>
            <li>
              <a class="dropdown-item" href="#"
                ><i class="japan flag"></i>日本語</a
                >
            </li>
            <li>
              <a class="dropdown-item" href="#"
                ><i class="germany flag"></i>Deutsch</a
                >
            </li>
            <li>
              <a class="dropdown-item" href="#"
                ><i class="france flag"></i>Français</a
                >
            </li>
            <li>
              <a class="dropdown-item" href="#"
                ><i class="spain flag"></i>Español</a
                >
            </li>
            <li>
              <a class="dropdown-item" href="#"
                ><i class="russia flag"></i>Русский</a
                >
            </li>
            <li>
              <a class="dropdown-item" href="#"
                ><i class="portugal flag"></i>Português</a
                >
            </li>
          </ul>
        </li>

        <!-- Avatar -->
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle hidden-arrow d-flex align-items-center" href="#" id="navbarDropdownMenuLink" role="button" data-mdb-toggle="dropdown" aria-expanded="false">
            <img src="https://mdbootstrap.com/img/Photos/Avatars/img (31).jpg" class="rounded-circle" height="22" alt="" loading="lazy" />
          </a>
          <ul class="dropdown-menu dropdown-menu-end" aria-labelledby="navbarDropdownMenuLink">
            <li><a class="dropdown-item" href="#">My profile</a></li>
            <li><a class="dropdown-item" href="#">Settings</a></li>
            <li><a class="dropdown-item" href="#">Logout</a></li>
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
