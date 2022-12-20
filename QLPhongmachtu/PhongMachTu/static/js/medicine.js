//
//function addMedicine() {
//        var name = document.getElementById("medicine").value
//        document.getElementById("ten").innerHTML = name
// }

$(document).ready(function() {
    $("#btnAdd").click(function() {
        var medicine = $("#medicineId").val()
        var type = $("#typeId").val()
        var amount = $("#amountId").val()
        var instruction = $("#instructionId").val()
        console.log(medicine)
        $("div.medicineArea").append(`
         <div class="row ">
              <input type="text" name="name_medicine" value='${medicine}'/>
              <input  type="text"  name="type" value='${type}'/>
              <input  type="text" name="amount" value='${amount}'/>
              <input  type="text" name="instruction" value='${instruction}'/>
              <div class="index-btn-sign">
                  <button type="button" class="btn btn-primary" >Xóa</button>
              </div>
         </div>
        `)
    })

    $("div.medicineArea").on("click","div.medicineArea input[type=button]",function() {
        if (confirm("Bạn có chắc chắn xóa không?") == true)
            $(this).parent().parent().remove()
    })
})






//function addMedicine(type,amount, instructions) {
//    let name = document.getElementById("medicine")
//    name = stringify(selectMedicine)
////    var selectSymptom = document.getElementById("symptom_medicine").value
////    var selectPredict = document.getElementById("predict_medicine").value
//    fetch('/api/add_medicine', {
//        method: 'post',
//        body: JSON.stringify ({
//            'id': id
//            'name_medicine':name.value,
//            'type_medicine':type,
//            'amount_medicine':amount,
//            'instructions_medicine':instructions
//        }),
//           headers: {
//           'Content-Type': 'application/json'}
//    }).then(function(res) {
//        console.info(res)
//        return res.json()
//    }).then(function(data) {
//        console.info(data)
//
//        var id = document.getElementById("id")
//        id.innerText = data.id
//        var name = document.getElementById("name")
//        name.innerText = data.name
//        var type = document.getElementById("type")
//        type.innerText = data.type
//        var amount = document.getElementById("amount")
//        amount.innerText = data.amount
//        var instructions = document.getElementById("instructions")
//        instructions.innerText = data.instructions
//
//    }).catch(function(err) {
//        console.error(err)
//    })
//}



//    if (name !== null) {
//        fetch('/api/add_medicine', {
//            method: 'post',
//            body: JSON.stringify({
//                'name':name
//            }),
//             headers: {
//                 'Content-Type': 'application/json'
//             }
//        }).then(res => res.json()).then(data => {
//              if (data.status == 201) {
//                   let c = data.medicine
//
//                   let area = document.getElementById('medicineArea')
//
//                   area.innerHTML =  area.innerHTML + `
//                        <div class="row">
//                            <div class="col-xs-5">
//                                <td>${stt}</td>
//                                <td>${c.name}</td>
//                                <td>
//                                    <select>
//                                    <option>Vỉ</option>
//                                    <option>Viên</option>
//                                    <option>Chai</option>
//                                </select>
//                                </td>
//                                <td><input type="number" ></td>
//                                <td><input type="text"></td>
//                            </div>
//                        </div>
//                    `
//                    stt = stt + 1
//                } else if (data.status == 404)
//                    alert(data.err_msg)
//             })

