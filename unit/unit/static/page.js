function stor() {
  let story = document.getElementById("story").value;
  console.log(story);
  if (story == "1") {
    document.getElementById("uu1").style.display = "none";
  } else {
    document.getElementById("uu1").style.display = "block";
  }
}

let boys = document.querySelector("#boys");
let girls = document.querySelector("#girls");
if (boys && girls) {
  boys.oninput = (e) => {
    addInputs(e.currentTarget, "boys");
  };
  girls.oninput = (e) => {
    addInputs(e.currentTarget, "girls");
  };
  let addInputs = (el, name) => {
    el.nextElementSibling.innerHTML = "";
    for (let i = 0; i < el.value; i++) {
      el.nextElementSibling.innerHTML += `
              <hr>
              <input class='form-control mb-2' name='${name}[${i}][name]' placeholder='الإسم'>
              <input class='form-control mb-2' name='${name}[${i}][age]' placeholder='السن'>
              <input class='form-control mb-2' name='${name}[${i}][national_id]' placeholder='الرقم القومي'>
          `;
    }
  };
}
