import { createRouter, createWebHistory } from 'vue-router'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    { path: '/', redirect: '/manager/home' },
    {
      path: '/manager',
      name: 'layout',
      component: () => import('@/layout/layout.vue'),
      children: [
        { path: 'home', name: 'home', component: () => import('@/views/home.vue') },
        { path: 'lab', name: 'lab', component: () => import('@/views/lab.vue') }
      ]
    },
    { path: '/login', name: 'Login', component: () => import('@/views/Login.vue') },
    { path: '/register', name: 'Register', component: () => import('@/views/Register.vue') }
  ]
})

export default router
