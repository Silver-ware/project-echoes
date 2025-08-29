import { createRouter, createWebHistory } from 'vue-router'
import CurateLayout from '@/layout/CurateLayout.vue'
import CurateView from '@/views/CurateView.vue'

const routes = [
  {
    path: '/',
    redirect: '/curate',
  },
  {
    path: '/curate',
    component: CurateLayout,
    name: 'Curate',
    children: [
      {
        path: '',
        name: 'CurateHome',
        component: CurateView,
        meta: { title: 'Curate Interface' },
      }
    ]
  }
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
