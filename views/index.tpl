%rebase('base.tpl')
%import model
<h1 style="font-size:50px;"><b>Spomin</b></h1>

<blockquote>
    <h3><i>Spomin je najboljša igra za urjenje spomina ;).</i></h3>
</blockquote>


<table>

    <tr>
        <td> <h4>Izberi težavnost: lahko=2, srednje=3, težko=4</td></h4>
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
