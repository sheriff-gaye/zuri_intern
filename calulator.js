

function calc(x,y,operator)
{
    if(operator=="+")
    {
        return x+y
    }
    else if(operator=="-")
    {
        return x-y
    }
    else if (operator=="*")
    {
        return x*y
    }
    else
    {
        return x-y
    }
}
var p=calc(5,6,'*') //it returns 30
