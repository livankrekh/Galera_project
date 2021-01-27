<template>
    <footer class="footer">
        <div class=" container">
            <hr class="border-white">
            <div class="row align-items-center justify-content-md-between text-white">
                <div class="col-md-6">
                    <div class="copyright">
                        &copy; {{year}}
                        <a href="https://www.brycen.co.jp/" target="_blank" rel="noopener">Brycen</a>
                    </div>
                </div>
            </div>
        </div>
    </footer>
</template>
<script>
export default {
  name: 'app-footer',
  data() {
    return {
      year: new Date().getFullYear()
    }
  }
};
</script>
<style>
</style>
