<script setup lang="ts">
import main from '@images/main.png'

const statistics = [
  {
    title: '기업 수',
    stats: '2707',
    icon: 'tabler-building-skyscraper',
    color: 'primary',
  },
  {
    title: '누적 사용자 수',
    stats: '3',
    icon: 'tabler-users',
    color: 'info',
  },
  {
    title: '채용 공고 수',
    stats: '30',
    icon: 'tabler-shopping-cart',
    color: 'error',
  },
  {
    title: '누적 채용 공고 조회 수',
    stats: '745',
    icon: 'tabler-eye-check',
    color: 'success',
  },
]
</script>

<template>
  <VRow>
    <VCol cols="12">
      <VCard title="Job A Dream">
        <VCardText>
          <VRow class="justify-center">
            <VCol cols="6">
              <VImg :src="main" />
            </VCol>
          </VRow>
        </VCardText>
        <VCardText>
          <h6 class=" text-h6">
            당신의 꿈을 "잡아 드림"
          </h6>
        </VCardText>
        <VCardText>
          <section>
            Job A Dream은 취업준비생들을 위한 취업 정보 제공 통합 플랫폼입니다.
          </section>
          <section>
            본 사이트는 취업 준비생들이 취업에 필요한 정보를 한눈에 볼 수 있도록 제공합니다.
          </section>
          <section>
            여러 채용 플랫폼에서 공고를 찾으러 다니지 않도록 Job A Dream에서 해당 기업의 채용공고를 한 눈이 볼 수 있도록 제공해드립니다.
          </section>
        </VCardText>
      </VCard>
    </VCol>
    <VCol cols="12">
      <VCard title="사이트 정보">
        <template #append>
          <span class="text-sm text-disabled">Updated 1 day ago</span>
        </template>

        <VCardText>
          <VRow>
            <VCol
              v-for="item in statistics"
              :key="item.title"
              cols="6"
              md="3"
            >
              <div class="d-flex">
                <VAvatar
                  :color="item.color"
                  variant="tonal"
                  size="42"
                  class="me-3"
                >
                  <VIcon :icon="item.icon" />
                </VAvatar>

                <div class="d-flex flex-column">
                  <span class="text-h5 font-weight-medium">{{ item.stats }}</span>
                  <span class="text-sm">
                    {{ item.title }}
                  </span>
                </div>
              </div>
            </VCol>
          </VRow>
        </VCardText>
      </VCard>
    </VCol>
  </VRow>
</template>
