<template>
    <div class="hello">
       <h3>{{ name }}</h3>
        <el-form :rules="tableForm.rules" :model="tableForm" ref="tableForm">
            <el-table
              :data="tableForm.tableData"
              style="width: 100%">
              <el-table-column
                prop="name"
                label="姓名"
                width="180">
              </el-table-column>
                <el-table-column
                label="年龄">
                    <template slot-scope="scope">
                        <el-form-item :prop="'tableData.'+scope.$index+'.age'" :rules="tableForm.rules.age">
                            <el-input-number
                                    size="mini"
                                    controls-position="right"
                                    :step=1
                                    v-model="scope.row.age"
                                    @change="changeAge(scope.$index, scope.row)"
                                    :min="0"
                                    :max="10"></el-input-number>
                        </el-form-item>
                    </template>
              </el-table-column>
            </el-table>
        </el-form>

    </div>
</template>

<script>
    export default {
        name:'',
        data(){
            return{
                name: "element-table-prac",
                tableForm:{
                     tableData: [{
                        date: '2016-05-02',
                        name: '王小虎',
                        address: '上海市普陀区金沙江路 1518 弄',
                        age:10
                      }, {
                        date: '2016-05-04',
                        name: '王小虎',
                        address: '上海市普陀区金沙江路 1517 弄',
                        age:10
                      }, {
                        date: '2016-05-01',
                        name: '王小虎',
                        address: '上海市普陀区金沙江路 1519 弄',
                        age:10
                      }, {
                        date: '2016-05-03',
                        name: '王小虎',
                        address: '上海市普陀区金沙江路 1516 弄',
                        age:12
                      }],
                    rules:{
                        age:[{type:'number', require:true, message:'年龄为必填项',trigger:'blur'},
                            {type:'number', max:99,min:0, message:'年龄必须为数字',trigger:'blur'}]
                    }

                }

            }
        },
        methods:{
            changeAge(index, row){
                console.log(index, row)
            }
        }

    }
</script>

<style scoped>

</style>