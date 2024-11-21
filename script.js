function calculateIntegral() {
    const expression = document.getElementById("expression").value;
    const variable = document.getElementById("variable").value;

    try {
        if (expression && variable) {
            // Use Nerdamer to calculate the integral
            const integral = nerdamer(`integrate(${expression}, ${variable})`).toString();
            document.getElementById("result").innerHTML = `The integral of ${expression} with respect to ${variable} is: ${integral}`;
        } else {
            document.getElementById("result").innerHTML = "Please enter both an expression and a variable.";
        }
    } catch (error) {
        document.getElementById("result").innerHTML = "Invalid expression or variable. Please try again.";
    }
}