%rebase('base.tpl')
%import model

<p><h1 style="font-size:50px;">Čestitke!</h1></p>
<p><h1 style="font-size:50px;">Zmagal/a si!</h1></p>


<table>

    <tr>
        <td><b>Če želiš igrati še enkrat, ponovno izberi težavnost!</b></td>
    </tr>
    
    <tr>
        <td>
            <form action="/nova_igra/" method="POST">
                <input type="radio" name="tezavnost" value="2"> Lahko<br>
                <input type="radio" name="tezavnost" value="3"> Srednje<br>
                <input type="radio" name="tezavnost" value="3"> Tezko<br>  
                <p><input type="submit" value="prični igro"></p>
            </form>
        </td>
    </tr>

    
</table>