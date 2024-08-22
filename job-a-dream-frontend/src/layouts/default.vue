<script lang="ts" setup>
import { switchToVerticalNavOnLtOverlayNavBreakpoint } from '@layouts/utils'

const DefaultLayoutWithHorizontalNav = defineAsyncComponent(() => import('./components/DefaultLayoutWithHorizontalNav.vue'))

// ℹ️ This will switch to vertical nav when define breakpoint is reached when in horizontal nav layout
// Remove below composable usage if you are not using horizontal nav layout in your app
switchToVerticalNavOnLtOverlayNavBreakpoint()

const { injectSkinClasses } = useSkins()

injectSkinClasses()
</script>

<template>
  <DefaultLayoutWithHorizontalNav />
</template>

<style lang="scss">
// As we are using `layouts` plugin we need its styles to be imported
@use "@layouts/styles/default-layout";
</style>
