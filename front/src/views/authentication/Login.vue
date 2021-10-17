<template>
  <base-home-page>
    <template #intro>
      <base-intro :isFullPage="true" :textWhite="true" :mask="0.5" src="https://images.pexels.com/photos/762084/pexels-photo-762084.jpeg?auto=compress&cs=tinysrgb&dpr=2&h=650&w=1200">
        <template>
          <authentication-form fieldType="email" :login="true" />
        </template>
      </base-intro>
    </template>
  </base-home-page>
</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      fields: [
        { type: 'email', placeholder: 'Email' },
        { type: 'password', placeholder: 'Password' },
      ]
    }
  }
}
</script>
