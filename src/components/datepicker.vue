<template>
    <div class="hello">
       <h3>{{ name }}</h3>
        <div class="block">
            <!--<span class="demonstration">多个日期</span>-->
            <el-date-picker
              type="dates"
              v-model="dates"
              @change="getdates"
              value-format="yyyy/MM/dd"
              placeholder="选择一个或多个日期">
            </el-date-picker>
        </div>
    </div>
</template>

<script>
    export default {
        name:'',
        data(){
            return{
                name: "日期选择器",
                dates:''

            }
        },
        methods:{
            getdates(){
                console.log(this.dates)
            }
        }

    }
</script>

<style scoped>

</style>